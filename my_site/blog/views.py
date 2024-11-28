from datetime import date
from django.shortcuts import render

# Create your views here.
all_posts = [
    {
        "slug":"deep-sea-diving",
        "image":"sea.jpg",
        "author":"Viper Price",
        "date": date(2024, 11, 28),
        "title":"Sea Touring",
        "excerpt":"The sea is calm and quiet. What about you?",
        "content": """
            Ut doloremque voluptates facilis dolorem autem molestiae expedita adipisci veritatis cumque nesciunt? Rem culpa saepe, sint rem veniam cumque omnis voluptates iste quo eius deserunt alias repellat, distinctio accusamus rem et eveniet illo vitae itaque a fuga odit inventore, saepe non laborum magni, dignissimos quidem eum animi voluptatibus sapiente vitae. Dolorum dolorem similique architecto in aut voluptates dolores suscipit itaque atque, molestiae hic soluta laborum sit consectetur id sequi architecto maxime, neque dignissimos numquam beatae temporibus, explicabo esse odit quas tenetur nam voluptate blanditiis libero? Ratione ut non delectus nisi in quos odio quis sed ipsam animi, voluptatibus cupiditate officia, consectetur ratione aspernatur quae?

            Magnam consectetur autem sunt doloremque doloribus nostrum optio quod at dolores, quisquam consequuntur alias, asperiores perferendis officiis voluptas voluptatum assumenda reiciendis soluta odio, quidem magnam ut? Repudiandae officiis neque eius ad quaerat porro eaque laborum dolorem, ab odit consectetur ut iste explicabo praesentium itaque? Atque accusantium ipsam cum dolorem nemo dolores veniam cumque nisi, in velit quo quasi dicta aspernatur numquam sapiente nam, sunt quibusdam rerum veniam ratione aliquid obcaecati architecto quisquam distinctio cum aperiam, illo veniam omnis tempore beatae, laborum numquam aliquid repellat sed ipsa quia.

            Autem nihil maiores quaerat incidunt officiis veritatis ipsam atque consequuntur, reprehenderit quidem numquam quam ut ratione odit non, id recusandae repudiandae aperiam alias hic soluta impedit, similique id assumenda laboriosam?

            Officia id ut beatae quam magnam dicta, laboriosam tempore odio quidem maxime?

            At aliquid suscipit praesentium? Nostrum facilis soluta natus repudiandae optio sint debitis ullam aut quis. Harum at eius itaque sit fugiat quidem quod aspernatur nam hic repellendus, omnis nulla natus facilis quae et dicta, fugit eius expedita debitis, ipsa itaque dolorum a cupiditate sed, itaque in cupiditate illo assumenda asperiores rerum?
            """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(posts):
    return posts["date"]

def starting_page(request):
    sorted_posts = sorted(all_posts, key = get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts                #传给这个html的值。记得看里面的for post in posts的posts！
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts               #传给这个all-posts.html。记得看里面的for post in posts的posts！
    })

def post_detail(request, slug):   #因为url那里设置了一个slug，所以这里必须传入
    identified_post = next(post for post in all_posts if post['slug']==slug)  #直接找all_posts里面post slug吻合的一项

    return render(request, "blog/post-detail.html", {
        "post":identified_post
    })
