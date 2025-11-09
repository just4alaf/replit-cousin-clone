from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/ask", methods=["POST"])
def ask():
    q = request.form.get("q", "").strip()
    if not q:
        return "<p class='text-red-600 font-medium'>Please enter a question.</p>"

        answer = ask_agent(q)
    return f"""<div class="p-6 bg-gradient-to-r from-green-50 to-emerald-50 dark:from-green-900 dark:to-emerald-900 rounded-xl shadow-inner"><p class="font-bold text-green-900 dark:text-green-100 mb-2">Answer:</p><pre class="p-4 bg-white dark:bg-gray-800 rounded-lg overflow-x-auto text-sm whitespace-pre-wrap border border-gray-200 dark:border-gray-700">{answer}</pre><button _="on click call navigator.clipboard.writeText(`{answer}`) then add .bg-green-600 to me then set my innerHTML to 'Copied!' then wait 2s then set my innerHTML to 'Copy' then remove .bg-green-600 from me" class="mt-3 px-4 py-2 bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 rounded-lg text-sm font-medium transition">Copy</button></div>"""
  <div class='p-5 bg-gradient-to-r from-blue-50 to-cyan-50 dark:from-blue-900 dark:to-cyan-900 rounded-xl shadow-md'>
    <p class='font-bold text-blue-900 dark:text-blue-100'>Question:</p>
    <p class='mt-1 text-blue-800 dark:text-blue-200'>{q}</p>
  </div>
  <div class='p-5 bg-gradient-to-r from-green-50 to-emerald-50 dark:from-green-900 dark:to-emerald-900 rounded-xl shadow-md'>
    <p class='font-bold text-green-900 dark:text-green-100'>Answer:</p>
    <p class='mt-1 text-green-800 dark:text-green-200'>
      Feature added! Check <code class='bg-white dark:bg-gray-800 px-2 py-1 rounded text-sm'>app.py</code>.
    </p>
  </div>
</div>"""

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5005))
    app.run(host="0.0.0.0", port=port, debug=True)

