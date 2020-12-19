from aiohttp import web
from .config import db_block, web_routes, render_html


@web_routes.get("/choose")
async def view_list_chooses(request):
    with db_block() as db:
        db.execute("""
        SELECT sn as stu_sn, name as stu_name FROM student ORDER BY name
        """)
        students = list(db)

        db.execute("""
        SELECT sn as cou_sn, name as cou_name FROM course ORDER BY name
        """)
        courses = list(db)

        db.execute("""
        SELECT ch.stu_sn, ch.cou_sn, 
            s.name as stu_name, 
            c.name as cou_name, 
        FROM student_course as ch
            INNER JOIN student as s ON ch.stu_sn = s.sn
            INNER JOIN course as c ON ch.cou_sn = c.sn
        ORDER BY stu_sn, cou_sn;
        """)

        items = list(db)

    return render_html(request, 'choose_list.html',
                       students=students,
                       courses=courses,
                       items=items)





@web_routes.get("/choose/delete/{stu_sn}/{cou_sn}")
def choose_deletion_dialog(request):
    stu_sn = request.match_info.get("stu_sn")
    cou_sn = request.match_info.get("cou_sn")
    if stu_sn is None or cou_sn is None:
        return web.HTTPBadRequest(text="stu_sn, cou_sn, must be required")

    with db_block() as db:
        db.execute("""
        SELECT ch.stu_sn, ch.cou_sn,
            s.name as stu_name, 
            c.name as cou_name,  
        FROM student_course as ch
            INNER JOIN student as s ON ch.stu_sn = s.sn
            INNER JOIN course as c  ON ch.cou_sn = c.sn
        WHERE stu_sn = %(stu_sn)s AND cou_sn = %(cou_sn)s;
        """, dict(stu_sn=stu_sn, cou_sn=cou_sn))

        record = db.fetch_first()

    if record is None:
        return web.HTTPNotFound(text=f"no such choose: stu_sn={stu_sn}, cou_sn={cou_sn}")

    return render_html(request, 'choose_dialog_deletion.html', record=record)
