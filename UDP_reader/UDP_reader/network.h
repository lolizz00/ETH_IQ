#ifndef _NETWORK_H_
#define _NETWORK_H_

#define _WINSOCK_DEPRECATED_NO_WARNINGS


#include <WinSock2.h>
#include <WS2tcpip.h>
#include <system_error>
#pragma comment (lib, "ws2_32.lib")

class WSASession
{
public:
	WSASession()
	{
		int ret = WSAStartup(MAKEWORD(2, 2), &data);
		if (ret != 0)
		{
			throw std::system_error(WSAGetLastError(), std::system_category(), "WSAStartup Failed");
		}
	}
	~WSASession()
	{
		WSACleanup();
	}
private:
	WSAData data;
};

class UDPSocket
{
public:
	UDPSocket()
	{
		sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
		if (sock == INVALID_SOCKET)
		{
			throw std::system_error(WSAGetLastError(), std::system_category(), "Error opening socket");
		}

		struct timeval tv;
		tv.tv_sec = 0;
		tv.tv_usec = 100000;

		if (setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, (char*)&tv, sizeof(tv)) < 0) 
		{
		}

	}
	~UDPSocket()
	{
		
	}

	void close()
	{
		closesocket(sock);
	}

	int RecvFrom(uint8_t* buffer, int len, int* cnt)
	{
		sockaddr  from;
		int ret = 0;


		int size = sizeof(from);
		*cnt = recvfrom(sock, (char*)buffer, len, 0, &from, &size);
		ret = WSAGetLastError();
		

		return ret;
	}
	void Bind(char* ip, unsigned short port)
	{
		sockaddr_in name;
		ZeroMemory(&name, sizeof(name));
		name.sin_family = AF_INET;
		name.sin_addr.S_un.S_addr = inet_addr(ip);
		name.sin_port = htons(port);
		
		int ret = bind(sock, (sockaddr*)&name, sizeof(name));
		if (ret < 0)
		{
			int tmp = WSAGetLastError();
//			cout << tmp << endl;
		}
	}

private:
	SOCKET sock;
};

#endif // !_NETWORK_H_
