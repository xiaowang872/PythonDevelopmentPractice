import asyncio # 导入所需的开发模块
# 服务端绑定了处理函数之后，会自动的出现读写操作的参数配置
async def echo_handler(reader, writer): # 定义ECHO消息的处理函数
    while True: # 持续的进行消息的交互处理
        # read()函数里面需要配置开辟的缓冲区的大小
        data = await reader.read(100) # 从客户端接收数据
        message = data.decode() # 数据的解码
        if message.lower() == 'exit': # 结束判断
            writer.close() # 关闭通道
            break # 退出循环
        # 客户端连接到服务器之后，服务端应该对当前的客户端进行响应
        # 因此每一个输出通道之中都会保存有客户端的访问地址信息
        client_address = writer.get_extra_info('peername') # 获取客户端地址
        print('【ECHO服务端】接收到来自“%s”的数据：%s' % (client_address, message))
        echo_message = '【ECHO】' + message # 服务端的回应内容
        writer.write(echo_message.encode()) # 进行编码操作
        await writer.drain() # 强制刷新缓冲区，进行内容的响应
async def main(): # 主函数
    # 设置绑定的主机为当前主机：127.0.0.1（localhost）为当前主机的地址（服务端绑定：0.0.0.0）
    server = await asyncio.start_server(
        echo_handler, '127.0.0.1', 8080) # 直接实现服务端运行
    server_address = server.sockets[0].getsockname() # 获取Socket名称
    print('ECHO服务端启动成功，监听地址为：%s' % str(server_address))
    async with server: # 让服务端持续运行
        await server.serve_forever() # 服务端持续运行
if __name__ == '__main__':  # Python程序运行起点
    asyncio.run(main()) # 调用主函数

# PS E:\summer_study\python开发\programe\pythonProject> & D:/python_install_file/python.exe e:/summer_study/python开发/programe/pythonProject/多协程编程/asyncio构建网络服务.py
# ECHO服务端启动成功，监听地址为：('127.0.0.1', 8080)

import asyncio # 导入所需的开发模块
async def main(): # 主函数
    # 此时在连接服务端之后，会返回读写两个通道的信息
    # 客户端的输出对于服务端来讲就是输入，同理，服务端的输出对于客户端来讲就是输入
    reader, writer = await asyncio.open_connection('127.0.0.1', 8080) # 连接网络
    while True: # 持续交互
        message = input('请输入要发送的信息：') # 等待键盘输入
        writer.write(message.encode()) # 发送消息给服务端
        await writer.drain() # 缓冲强制性刷新（输出）
        data = await reader.read(100) # 等待服务端响应
        print(data.decode()) # 消息解码
        if message.lower() == 'exit': # 结束处理
            break; # 退出循环
    print('关闭网络连接，本次交互结束')
    writer.close() # 关闭输出流
    await writer.wait_closed() # 关闭连接
if __name__ == '__main__':  # Python程序运行起点
    asyncio.run(main()) # 调用主函数

