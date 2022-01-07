import re

my_string = "I am a very very good boy. I lives in India."
my_password = "g@uiopT%_!WEB"
my_email = "test1234_ee@email.co.in"

x = re.findall("[Ii]n", my_string)
print(x)

y = re.search(r"\s", my_string)
print(f"start position: {y.start()}, End position: {y.end()}, Group: {y.group()}, Span is: {y.span()}, "
      f"String: {y.string}")

z = re.finditer("er", my_string)
for item in z:
    print(f"start position: {item.start()}, End position: {item.end()}, Group: {item.group()}, Span is: {item.span()},"
          f" String: {item.string}")

a = re.split(r"\s", my_string, maxsplit=2)
print(a)

b = re.sub(r"\s", "--", my_string)
print(b)