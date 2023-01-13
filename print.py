import requests
print(requests.__version__)
response = requests.get("http://google.com")
print(response.content)
get_script = requests.get("https://raw.githubusercontent.com/ZhiyuanYu133/Cmput404/main/print.py")
print(get_script.text)
