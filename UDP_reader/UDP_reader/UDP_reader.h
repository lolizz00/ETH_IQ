#ifndef _UDP_READER_H_
#define _UDP_READER_H_
#define _CRT_SECURE_NO_WARNINGS

#include <stdint.h>
#include <stdlib.h>


#include <SDKDDKVer.h>

using namespace std;

// ---

#define BUFLEN 8096
#define BUFSIZE 10000
#define ADDR "192.168.18.70"
#define PORT 4000


// ---

#include "network.h"

#include <thread>
#include <vector>
#include <mutex>
#include <string> 

#include <direct.h>

/* --- ���������� ---*/

#define DLLEXPORT __declspec(dllexport)
extern "C"
{
	DLLEXPORT int READER_read(int n);
}

#endif //  _UDP_READER_H_
