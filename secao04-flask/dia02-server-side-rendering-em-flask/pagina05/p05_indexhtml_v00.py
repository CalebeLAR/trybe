# ...
#     <img src="{{ url_for('static', filename='images/logo.png') }}" width="40%">

# -    <form action="/" method="post">
# +    <form action="/chat" method="post">
#         <p>Olá {{username|capitalize|trim}}! {{greeting}}, como você se chama?</p>
#         <div class="send-box">
#             <input type="text" name="username">
# ...