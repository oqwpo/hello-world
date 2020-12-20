#include<stdio.h>
#include<windows.h>
#include<conio.h>
int main(void)
{
    char c;
    int x=1,y=1;
    char s[5][10]=
    {
        "##########",
        "#s       #",
        "### ## ###",
        "#   #  ###",
        "### ## ###",
    };
    while(1)
    {
        for (int i = 0; i < 5; i++)
        {
            for(int j=0;j<10;j++)
            printf("%c",s[i][j]);
            printf("\n");
        }
        
        c=getch();
        if(c=='d')
            if (s[x][y]!='#')
            {
                s[x][y]=' ';
                y+=1;
                s[x][y]='s';
            }
        if(c=='s')
            if (s[x][y]!='#')
            {
                s[x][y]=' ';
                x+=1;
                s[x][y]='s';
            }
        if(c=='a')
            if (s[x][y]!='#')
            {
                s[x][y]=' ';
                y-=1;
                s[x][y]='s';
            }
        if(c=='w')
            if (s[x][y]!='#')
            {
                s[x][y]=' ';
                x-=1;
                s[x][y]='s';
            }
        system("cls");    
    }
    return 0;
}