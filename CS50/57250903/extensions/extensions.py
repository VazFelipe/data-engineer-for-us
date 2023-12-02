# Requirements
## if the user prompts a filename named
## *.gif then use MIME Type image/gif
## same behavior for *.jpg, *.jpeg, *.png, *.pdf, *.txt, *.zip
## MIME Types in https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types

def main():
    print(apply_mime_type())

def prompt_user():
    return input('File name: ')

def apply_mime_type():
    import mimetypes
    prompt_from_user = prompt_user().lower().strip()
    if '.' not in prompt_from_user:
        return 'application/octet-stream'
    else:
        mime_type = mimetypes.guess_type(url=prompt_from_user, strict=True)
        return mime_type[0]

main()