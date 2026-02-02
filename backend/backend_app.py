from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows your local frontend to talk to this Codio backend

# Our "Database" - a simple list of dictionaries
POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


# --- HELPER FUNCTION FOR SORTING ---
# We use this instead of a Lambda function to make the logic clear
def get_sort_key(post):
    """
    This function acts as a 'scout'. For every post in the list,
    it grabs the specific field the user wants to sort by.
    """
    # 'sort_field' is defined inside the handle_posts() function below
    field_to_look_at = request.args.get('sort')

    # We grab the text (title or content) and make it lowercase
    # so that 'A' and 'a' are treated the same way.
    return post[field_to_look_at].lower()


@app.route('/api/posts', methods=['GET', 'POST'])
def handle_posts():
    """Main route for Listing (GET) and Adding (POST) posts."""

    if request.method == 'GET':
        # 1. Look at the URL to see if there are sorting instructions
        sort_field = request.args.get('sort')
        direction = request.args.get('direction', 'asc')

        # 2. Start with a copy of our posts
        results = list(POSTS)

        # 3. If the user provided a sort field, start the sorting process
        if sort_field:
            # Error Check: Make sure they didn't type a field that doesn't exist
            if sort_field not in ['title', 'content']:
                return jsonify({"error": f"Invalid sort field: {sort_field}"}), 400

            # Determine if we should flip the list (descending)
            is_reverse = True if direction == 'desc' else False

            # Use our helper function (get_sort_key) to organize the list
            results = sorted(POSTS, key=get_sort_key, reverse=is_reverse)

        return jsonify(results)

    if request.method == 'POST':
        # 1. Open the JSON package sent by the user
        data = request.get_json()

        # 2. Validation: Ensure title and content are both there
        if not data or 'title' not in data or 'content' not in data:
            return jsonify({"error": "Missing 'title' or 'content'"}), 400

        # 3. Generate a new ID by adding 1 to the highest current ID
        new_id = max(post['id'] for post in POSTS) + 1 if POSTS else 1

        # 4. Create the new post dictionary
        new_post = {
            "id": new_id,
            "title": data['title'],
            "content": data['content']
        }

        # 5. Save it to our master list and return success
        POSTS.append(new_post)
        return jsonify(new_post), 201


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    """Filters posts based on search terms in the URL."""
    # 1. Grab search terms from the URL (?title=...&content=...)
    t_query = request.args.get('title', '').lower()
    c_query = request.args.get('content', '').lower()

    # 2. Loop through posts and keep only those that match the search
    filtered = []
    for post in POSTS:
        title_match = t_query in post['title'].lower() if t_query else True
        content_match = c_query in post['content'].lower() if c_query else True

        if title_match and content_match:
            filtered.append(post)

    return jsonify(filtered)


@app.route('/api/posts/<int:id>', methods=['PUT', 'DELETE'])
def handle_single_post(id):
    """Handles updating or deleting a specific post using its ID."""
    global POSTS  # Required so we can modify the master list

    # 1. Find the post that matches the ID in the URL
    post = next((p for p in POSTS if p['id'] == id), None)

    # 2. If the post doesn't exist, stop and return 404
    if post is None:
        return jsonify({"error": f"Post with id {id} not found"}), 404

    if request.method == 'PUT':
        # 1. Get the new data
        new_data = request.get_json()

        # 2. Update the values (use old values if new ones weren't sent)
        post['title'] = new_data.get('title', post['title'])
        post['content'] = new_data.get('content', post['content'])
        return jsonify(post), 200

    if request.method == 'DELETE':
        # 1. Create a new list that EXCLUDES the post with this ID
        POSTS = [p for p in POSTS if p['id'] != id]
        return jsonify({"message": f"Post with id {id} deleted successfully."}), 200


if __name__ == '__main__':
    # Running on 0.0.0.0 is necessary for Codio's Public URL to work
    app.run(host="0.0.0.0", port=5002, debug=True)