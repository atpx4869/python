from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form["keyword"]
        df1 = pd.read_excel("data1.xlsx")
        df2 = pd.read_excel("data2.xlsx")

        # 合并多个 DataFrame 对象
        df = pd.concat([df1, df2], axis=0, ignore_index=True)
        query = df[df['检测标准'].str.contains(keyword, na=False)]
        return render_template("index.html", keyword=keyword, query=query.to_html(index=False))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)