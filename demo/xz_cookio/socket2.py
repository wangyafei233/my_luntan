# coding:utf-8
import paramiko
import threading

# 设置ssh连接的远程主机地址和端口

ip = '192.168.124.241'
port = 22
username = 'peter'
password = 'peter123'
session_timeout = 60
t = paramiko.Transport((ip, port))
# 设置登录名和密码
t.connect(username=username, password=password)
# 连接成功后打开一个channel
chan = t.open_session()
# 设置会话超时时间
chan.settimeout(0.2)
# 打开远程的terminal
chan.get_pty()
# 激活terminal
chan.invoke_shell()


# 然后就可以通过chan.send('command')和chan.recv(recv_buffer)来远程执行命令以及本地获取反馈。
# 例如：
def recive(channel):
    while 1:
        if channel.recv_ready():
            try:
                print(channel.recv(65535).decode())
            except:
                pass


def send(channel):
    while 1:
        temp = input()
        channel.send(temp + '\n')


threads = []
t1 = threading.Thread(target=recive, args=(chan,))
threads.append(t1)
t2 = threading.Thread(target=send, args=(chan,))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
