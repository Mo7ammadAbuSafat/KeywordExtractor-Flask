from flask import Flask, request, jsonify
from KeywordExtractor import KeywordExtractor
import asyncio

app = Flask(__name__)
keyword_extractor = KeywordExtractor()


@app.route('/process_text', methods=['GET'])
async def process_text():
    text = request.args.get('text')
    result = await keyword_extractor.extract(text)
    return jsonify(keywords=result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(keyword_extractor.setup())
    app.run(debug=True, port=5000)
