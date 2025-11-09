#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define INF 1000000000
#define V 8

typedef struct { int u,v,w; } Edge;
int cmp(const void*a,const void*b){
  const Edge*A=a,*B=b;
  int au=A->u<A->v?A->u:A->v, av=A->u<A->v?A->v:A->u;
  int bu=B->u<B->v?B->u:B->v, bv=B->u<B->v?B->v:B->u;
  if(au!=bu) return au-bu; return av-bv;
}

int main(void){
  int G[V][V];
  for(int i=0;i<V;i++) for(int j=0;j<V;j++) G[i][j]=INF;
  for(int i=0;i<V;i++) G[i][i]=INF;

  // --- РЕБРА ---
  G[0][2]=G[2][0]=1; // 1-3
  G[2][7]=G[7][2]=4; // 3-8
  G[7][6]=G[6][7]=5; // 8-7
  G[6][4]=G[4][6]=4; // 7-5
  G[4][3]=G[3][4]=1; // 5-4
  G[3][0]=G[0][3]=4; // 4-1
  G[0][1]=G[1][0]=4; // 1-2
  G[2][3]=G[3][2]=5; // 3-4
  G[1][5]=G[5][1]=3; // 2-6
  G[1][4]=G[4][1]=7; // 2-5
  G[2][5]=G[5][2]=5; // 3-6
  G[5][6]=G[6][5]=6; // 6-7
  // ------------------

  bool sel[V]={0}; sel[0]=true;
  Edge mst[V]; int used=0,total=0;

  printf("Edge (u-v)  Weight\n");
  while(used<V-1){
    int best=INF,bu=-1,bv=-1;
    for(int u=0;u<V;u++) if(sel[u])
      for(int v=0;v<V;v++) if(!sel[v] && G[u][v]<best){
        best=G[u][v]; bu=u; bv=v;
      }
    sel[bv]=true; mst[used]=(Edge){bu,bv,best}; total+=best; used++;
    printf("%d - %d       %d\n", bu+1,bv+1,best);
  }
  printf("\nTotal weight = %d\n", total);

  qsort(mst,V-1,sizeof(Edge),cmp);
  printf("MST edges (sorted):\n");
  for(int i=0;i<V-1;i++){
    int a=mst[i].u+1,b=mst[i].v+1; if(a>b){int t=a;a=b;b=t;}
    printf("(%d-%d)=%d\n",a,b,mst[i].w);
  }
  return 0;
}
