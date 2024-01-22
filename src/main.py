import base64
import requests


def merge_contents(links, filename):
    contents = ""
    for link in links:
        response = requests.get(link)
        # 如果响应状态码为200，表示请求成功
        if response.status_code == 200:
            # 获取响应内容的文本
            text = response.content.decode()
            decoded = base64.urlsafe_b64decode(text)
            text = decoded.decode()
            contents += text + "\n"
        else:
            raise Exception(f"请求失败，状态码为{response.status_code}")
    with open(filename, "w", encoding="utf-8") as f:
        b64context = base64.urlsafe_b64encode(contents.encode())
        # 将合并的内容写入到文件中
        f.write(b64context.decode())
    with open('testno64.txt', "w", encoding="utf-8") as j:
        j.write(contents)

# 定义一个主函数，用于执行程序的逻辑
def main():
    # 定义一个常量，表示要提取链接的url

    # 定义一个常量，表示要合并内容的文件名
    filename = "test.txt"
    # 调用extract_links函数，从url中提取链接
    links = {'https://raw.githubusercontent.com/wentao883/TG-wxgqlfx_BYDY/main/pdyjdy_BYDY',
             'https://raw.githubusercontent.com/wentao883/TG-wxgqlfx_LSDY/main/pdyjdy_LSDY',
             'https://raw.githubusercontent.com/wentao883/TG-wxgqlfx_ZDY/main/pdyjdy_ZDY'}
    #  print(links)
    # 调用merge_contents函数，从链接中获取内容，并合并到文件中
    merge_contents(links, filename)
    # 打印一个提示信息，表示程序执行成功
    print(f"程序执行成功，内容已合并到{filename}文件中")


# 如果这个文件是作为主程序运行，调用main函数
if __name__ == "__main__":
    main()
