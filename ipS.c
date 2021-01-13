// server program for udp connection 
#include <stdio.h> 
#include <strings.h> 
#include <sys/types.h> 
#include <arpa/inet.h> 
#include <sys/socket.h> 
#include<netinet/in.h> 
#define PORT 5000 
#define MAXLINE 1000 

char findClass(char str[]) 
{ 
    // storing first octet in arr[] variable 
    char arr[4]; 
    int i = 0; 
    while (str[i] != '.') 
    { 
        arr[i] = str[i]; 
        i++; 
    } 
    i--; 
  
    // converting str[] variable into number for 
    // comparison 
    int ip = 0, j = 1; 
    while (i >= 0) 
    { 
        ip = ip + (str[i] - '0') * j; 
        j = j * 10; 
        i--; 
    } 
  
    // Class A 
    if (ip >=1 && ip <= 126) 
        return 'A'; 
  
    // Class B 
    else if (ip >= 128 && ip <= 191) 
        return 'B'; 
  
    // Class C 
    else if (ip >= 192 && ip <= 223) 
        return 'C'; 
  
    // Class D 
    else if (ip >= 224 && ip <= 239) 
        return 'D'; 
  
    // Class E 
    else
        return 'E'; 
} 

void separate(char str[], char ipClass) 
{ 
    // Initializing network and host array to NULL 
    char network[12], host[12]; 
    for (int k = 0; k < 12; k++) 
        network[k] = host[k] = '\0'; 
  
    // for class A, only first octet is Network ID 
    // and rest are Host ID 
    if (ipClass == 'A') 
    { 
        int i = 0, j = 0; 
        while (str[j] != '.') 
            network[i++] = str[j++]; 
        i = 0; 
        j++; 
        while (str[j] != '\0') 
            host[i++] = str[j++]; 
        printf("Network ID is %s\n", network); 
        printf("Host ID is %s\n", host); 
    } 
  
    // for class B, first two octet are Network ID 
    // and rest are Host ID 
    else if (ipClass == 'B') 
    { 
        int i = 0, j = 0, dotCount = 0; 
  
        // storing in network[] up to 2nd dot 
        // dotCount keeps track of number of 
        // dots or octets passed 
        while (dotCount < 2) 
        { 
            network[i++] = str[j++]; 
            if (str[j] == '.') 
                dotCount++; 
        } 
        i = 0; 
        j++; 
  
        while (str[j] != '\0') 
            host[i++] = str[j++]; 
  
        printf("Network ID is %s\n", network); 
        printf("Host ID is %s\n", host); 
    } 
  
    // for class C, first three octet are Network ID 
    // and rest are Host ID 
    else if (ipClass == 'C') 
    { 
        int i = 0, j = 0, dotCount = 0; 
  
        // storing in network[] up to 3rd dot 
        // dotCount keeps track of number of 
        // dots or octets passed 
        while (dotCount < 3) 
        { 
            network[i++] = str[j++]; 
            if (str[j] == '.') 
                dotCount++; 
        } 
  
        i = 0; 
        j++; 
  
        while (str[j] != '\0') 
            host[i++] = str[j++]; 
  
        printf("Network ID is %s\n", network); 
        printf("Host ID is %s\n", host); 
    } 
  
    // Class D and E are not divided in Network 
    // and Host ID 
    else
        printf("In this Class, IP address is not"
           " divided into Network and Host ID\n"); 
} 

// Driver code 
int main() 
{    
    char buffer[100]; 
    char *message; 
    int listenfd, len; 
    struct sockaddr_in servaddr, cliaddr; 
    bzero(&servaddr, sizeof(servaddr)); 
  
    // Create a UDP Socket 
    listenfd = socket(AF_INET, SOCK_DGRAM, 0);         
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY); 
    servaddr.sin_port = htons(PORT); 
    servaddr.sin_family = AF_INET;  
   
    // bind server address to socket descriptor 
    bind(listenfd, (struct sockaddr*)&servaddr, sizeof(servaddr)); 
       
    //receive the datagram 
    len = sizeof(cliaddr); 
    int n = recvfrom(listenfd, buffer, sizeof(buffer), 
            0, (struct sockaddr*)&cliaddr,&len); //receive message from server 
    buffer[n] = '\0'; 
    puts(buffer); 
           
    //logic to check which type is it
    message = separate(buffer,findClass(buffer));
    // send the response 
    sendto(listenfd, message, MAXLINE, 0, 
          (struct sockaddr*)&cliaddr, sizeof(cliaddr)); 
}