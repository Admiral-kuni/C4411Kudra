import requests
res_parse_list = []

response = requests.get("https://coinmarketcap.com/")
responce_text = response.text
responce_parse = responce_text.split("<span>")
print(response.text)
for parse_elem_1 in responce_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                print(parse_elem_2)
            res_parse_list.append(parse_elem_2)
    print(f"Bitcoin: {res_parse_list[0]}")