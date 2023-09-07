from parsel import Selector
import requests


response = requests.get("https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/3d93d491-e3ed-409f-bdb6-3a5dcd11f8d2/section/61c046bb-0372-49d7-83c1-fe68b9e01d73/day/29e6c74d-baff-46b1-9880-3ce81ab1a33e/lesson/02f58450-7939-4f66-aa1d-35ee475efa45")
print(response.status_code)
# selector = Selector(text=response.text)

print(response.text)