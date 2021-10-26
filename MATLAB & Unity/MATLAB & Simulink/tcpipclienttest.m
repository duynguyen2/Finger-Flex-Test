clc
clear all
tcpipServer = tcpip('0.0.0.0', 55000, 'NetworkRole', 'Server');


while(1)
    data = membrane(1);
    fopen(tcpipServer);
    rawData = fread(tcpipServer, 14, 'char');
    for i=1:14
        newData(i)= char(rawData(i));
    end
    if strlength(newData) == 14
        disp(newData);
        fclose(tcpipServer);
        break;
    end
    fclose(tcpipServer);
end