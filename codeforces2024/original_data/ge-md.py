import os
from bs4 import BeautifulSoup
import html2text


def remove_extra_blank_lines(markdown_text):
    """
    移除 Markdown 文本中连续的两个或更多空行，减少为一个空行。
    """
    lines = markdown_text.splitlines()
    cleaned_lines = []
    for line in lines:
        if not line.strip():  # 当前行是空行
            if cleaned_lines and not cleaned_lines[-1].strip():
                continue  # 如果上一行也是空行，跳过当前行
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def convert_html_to_markdown(html_file, output_file):
    """
    将 HTML 文件转换为 Markdown 文件并保存。
    """
    try:
        with open(html_file, "r", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')

        # 移除无关的 MathJax 元素
        for tag in soup.select(".MathJax_Preview, .MJX_Assistive_MathML, span.MathJax"):
            tag.decompose()

        for script_tag in soup.find_all("script", attrs={"type": "math/tex"}):
            if script_tag.string:
                script_tag.replace_with(script_tag.string + " ")
            else:
                script_tag.decompose()

        # 使用 html2text 转换 HTML 为 Markdown
        h2t = html2text.HTML2Text()
        markdown_text = h2t.handle(str(soup))
        markdown_text = remove_extra_blank_lines(markdown_text)

        # 保存为 Markdown 文件
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown_text)
        print(f"Converted: {html_file} -> {output_file}")
    except Exception as e:
        print(f"Error processing {html_file}: {e}")


def process_folders_for_html_to_md_conversion(start, end):
    """
    遍历当前目录及范围内的数字子文件夹，将所有 HTML 文件转换为 Markdown 文件。
    """
    current_dir = os.getcwd()

    # 获取指定范围内的数字文件夹
    subfolders = [f.path for f in os.scandir(current_dir) if f.is_dir() and f.name.isdigit() and start <= int(f.name) <= end]

    for folder in subfolders:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".html"):
                    html_file = os.path.join(root, file)
                    md_file = os.path.splitext(html_file)[0] + ".md"
                    convert_html_to_markdown(html_file, md_file)


if __name__ == "__main__":
    # 指定范围 1919-1920
    start_range = 1951
    end_range = 1980
    process_folders_for_html_to_md_conversion(start_range, end_range)
