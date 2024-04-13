#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import argparse
import numpy as np
import matplotlib.pyplot as plt

# 参考URL

def out_3dgraph( XX, YY, ZZ, show=False, fpath="axes3d.png", debug=False ):
    
    fig = plt.figure()
    ax = fig.add_subplot( 111, projection='3d' ) # projection='3d'とすることで、Axesオブジェクトの3D版のAxes3Dオブジェクトを生成できる
    
    if debug: print( f"type(fig)={type(fig)}, type(ax)={type(ax)}" ) #=> type(fig)=<class 'matplotlib.figure.Figure'>, type(ax)=<class 'mpl_toolkits.mplot3d.axes3d.Axes3D'> ※通常：type(ax)=<class 'matplotlib.axes._axes.Axes'>
    if debug: print( f"fig.get_figwidth()={fig.get_figwidth()}, fig.get_figheight()={fig.get_figheight()}, fig.get_dpi()={fig.get_dpi()}" ) #=> fig.get_figwidth()=6.4, fig.get_figheight()=4.8, fig.get_dpi()=100.0
    
    ax.set_xlabel( "X" )
    ax.set_ylabel( "Y" )
    ax.set_zlabel( "Z" )
    
    #fig.savefig( "axes3d_only_fig.png" ) #=> 640x480の3次元のグラフが出力された
    
    ax.plot_wireframe( XX, YY, ZZ )
    
    if show:
        plt.show()
    
    fig.savefig( fpath )

def main( args ):
    
    def func1( xx, yy ):
        
        return xx ** 2 + yy ** 2
    
    def func2( xx, yy ):
        
        # リスト 3.1 の f1
        
        return 4 * xx**2 + 4 * yy**2
    
    def func3( xx, yy ):
        
        # リスト 3.1 の f2
        
        return (xx - 5)**2 + (yy - 5)**2
    
    # データ準備
    xx = np.arange( float(args.graph_xlim[0]), float(args.graph_xlim[1]) + 0.1, 0.1 )
    yy = np.arange( float(args.graph_ylim[0]), float(args.graph_ylim[1]) + 0.1, 0.1 )
    
    XX, YY = np.meshgrid( xx, yy ) # 2次元の格子座標を生成する (XY座標で、X=-3から3、Y=-3から3までの0.1刻みで全組み合わせ)
    
    lst_func = [ func1, func2, func3 ]
    
    ZZ = lst_func[args.pat]( XX, YY )
    
    print( f"XX.shape={XX.shape}, YY.shape={YY.shape}" )
    print( f"XX={XX}" )
    print( f"YY={YY}" )
    
    # 出力ファイル名
    if args.fpath_out is None:
        args.fpath_out = f"axes3d_{args.pat}.png"
    
    # グラフ描画
    out_3dgraph( XX, YY, ZZ, show=args.show, fpath=args.fpath_out )

def parse_args():
    
    parser = argparse.ArgumentParser( description='axes3d' )
    
    parser.add_argument( '--pat',        default=0,       type=int,  help='pattern'         )
    parser.add_argument( '--fpath_in',   default=None,               help='input file path' )
    parser.add_argument( '--fpath_out',  default=None,               help='save file path'  )
    parser.add_argument( '--graph_xlim', default=[-3, 3], nargs='*', help='input xlim list' )
    parser.add_argument( '--graph_ylim', default=[-3, 3], nargs='*', help='input ylim list' )
    parser.add_argument( '--show',       default=False, action="store_true", help='show graph' )
    
    return parser.parse_args()

if __name__ == "__main__":
    
    args = parse_args()
    print( "args=", args )
    
    # 実行例
    # ・x**2 + y**2
    #   $ python --pat
    # ・リスト3.1のf1
    # ・リスト3.1のf2
    
    main( args )
