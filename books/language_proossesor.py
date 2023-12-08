from locals import lang_packages

def lang_control(request):
    url =  request.get_full_path()  #"/admin/ru/about/12/"
    lang = url.strip('/').split('/')[0]
    if lang in ['en','ru',"uz"]:
        return lang_packages[lang]
    return {}

