import re

s1 = "HeHelHellHelll"
s2 = "HellWorld"
# 第一种
# print(re.findall("Hel*", s1))

# 第二种
# pattern = re.compile("Hel*")
# print(pattern.findall(s1))
# print(pattern.findall(s2))


s = "<div class='user-avatar J-login'>\
              <img src='https://p0.meituan.net/movie/7dd82a16316ab32c8359debdb04396ef2897.png'>\
              <span class='caret'></span>\
              <ul class='user-menu no-login-menu'>\
                <li><a href='javascript:void 0'>ere</a></li>\
              </ul>\
            </div>"
# pattern = re.compile("src=\'.*\.png")
pattern = re.compile("src=\'(.*\.png)")
print(pattern.findall(s))
