for module in \
"printed_txt" \
:
    try:
        exec(f"import {module}")
    except:
        continue