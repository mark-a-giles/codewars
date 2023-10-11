import re
def domain_name(url):
    result = re.search('(?<=//)(.*)(?=.com)', url)
    try:
        return result.group(0)
    except:
        return None

result = domain_name('https://github.com')
print(result)