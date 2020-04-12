#
# from qa_interface_test.models import AutoInterfaceRecord
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
# import datetime
# security_account = '1571645388@qq.com'  # 发件人邮箱账号
# security_password = 'uyltirninhczjige'  # 发件人邮箱密码
# receiver = '1571645388@qq.com'  # 收件人邮箱账号，我这边发送给自己
#
# def mail():
#     ret = True
#     try:
#         query = AutoInterfaceRecord.objects.all()
#         msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
#         msg['From'] = formataddr(["来自方圻程", security_account])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To'] = formataddr(["发送至研发团队", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject'] = "测试执行日期"+str(datetime.datetime.now()) # 邮件的主题，也可以说是标题
#
#         server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
#         server.login(security_account, security_password)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(security_account, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()  # 关闭连接
#     except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret = False
#     return ret
#
# ret = mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")
