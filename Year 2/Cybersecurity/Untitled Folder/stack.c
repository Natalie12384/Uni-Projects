/* stack.c */
/* This program has a buffer overflow vulnerability. */
/* Our task is to exploit this vulnerability */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int bof(char *str, int studentId)
{
int bufferSize; //4 bytes
bufferSize = 12 + studentId%32; //=36
char buffer[bufferSize]; //36 bytes
/* The following statement has a buffer overflow problem */
strcpy(buffer, str);

return 1;
}

int main(int argc, char **argv) //return add: 0x08048584
{
char str[517]; //maybe remove nops
FILE *badfile;
int studentId = 33095000;// please put your student ID
badfile = fopen("badfile", "r"); //takes an input from bad file, passes to buffer
fread(str, sizeof(char), 517, badfile);//put char of badfile into str destination
bof(str,studentId);//call function bof
printf("Returned Properly\n");
return 1;
}
