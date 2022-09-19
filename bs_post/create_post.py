import pyodbc
import datetime

conn = pyodbc.connect('Driver={SQL Server};'
        'Server=MSI\SQLEXPRESS;'
        'Database=blog_site;'
        'Trusted_Connection=yes;')

cur = conn.cursor()

authorId = 2
title = "Full Stack Development Roadmap"
content = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
createdAt = str(datetime.datetime.now())[:19+4]
updatedAt = str(datetime.datetime.now())[:19+4]
publishedAt = str(datetime.datetime.now())[:19+4]

sql = f"""insert into bs_post(
authorId,
title,
content,
createdAt,
updatedAt,
publishedAt
) 
values
(
'{authorId}',
'{title}',
'{content}',
'{createdAt}',
'{updatedAt}',
'{publishedAt}'
);
"""

cur.execute(sql)

conn.commit()
conn.close()