clc
clear all
%tcpipClient = tcpclient('127.0.0.1', 55001, 'ConnectTimeout', 20);
tcpipClient = tcpip('127.0.0.1', 55001, 'NetworkRole', 'client');
set(tcpipClient, 'Timeout', 30);
fopen(tcpipClient);
a = 'nice job bozo';
%tcpipClient.write(a);
fwrite(tcpipClient, a);
fclose(tcpipClient);
%tcpipClient.flush();