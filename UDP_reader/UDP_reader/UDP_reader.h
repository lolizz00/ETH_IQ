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
extern char* ADDR;
#define PORT 4000


// ---

#include "network.h"

#include <thread>
#include <vector>
#include <mutex>
#include <string> 

#include <direct.h>

/* --- Библиотека ---*/

#define DLLEXPORT __declspec(dllexport)
extern "C"
{
	DLLEXPORT int READER_read(int n,char* _ADDR);
}

#endif //  _UDP_READER_H_
