"""Minimal English/Cebuano switch for navigation and key buttons.
Have a native Cebuano speaker review these before launch."""

EN = {
    "services": "Services", "calculator": "Loan calculator", "branches": "Branches", "stories": "Stories",
    "faqs": "FAQs", "forms": "Forms", "news": "News", "contact": "Contact", "login": "Log in",
    "logout": "Log out", "apply": "Apply", "my_apps": "My applications", "become_member": "Become a member",
    "find_branch": "Find a branch",
}
CEB = {
    "services": "Serbisyo", "calculator": "Kalkulyador sa Utang", "branches": "Mga Sanga",
    "stories": "Mga Istorya", "faqs": "Mga Pangutana", "forms": "Mga Porma", "news": "Balita",
    "contact": "Kontaka", "login": "Pag-log in", "logout": "Pag-log out", "apply": "Mag-apply",
    "my_apps": "Akong mga Aplikasyon", "become_member": "Mahimong Membro", "find_branch": "Pangitaa ang Sanga",
}


def lang(request):
    code = request.COOKIES.get("lang", "en")
    return {"t": {**EN, **CEB} if code == "ceb" else EN, "lang": code}
