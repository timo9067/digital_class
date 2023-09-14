def generate_cat_list(res_count):
    res = ""
    for cat in res_count:
        res += f"<li>{cat['cat_id__cat']}: {cat['count_cat']}</li>"
        
    return res