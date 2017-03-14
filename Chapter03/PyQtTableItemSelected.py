# -*- coding: utf-8 -*- 
'''
    【简介】
	PyQT5的表格控件选中单元格
  
    作者：信平
    QQ： 759949947	
    Email: xpws2006@163.com   
  
'''

import sys
from PyQt5.QtWidgets import  *
from PyQt5 import QtCore  
from PyQt5.QtGui import  QColor , QBrush

class Table(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget demo")
        self.resize(600,800);
        conLayout = QHBoxLayout()
        tableWidget= QTableWidget()
        tableWidget.setRowCount(35)
        tableWidget.setColumnCount(4)
        conLayout.addWidget(tableWidget )
        
        for i in range(35):
            for j in range(4):
                itemContent = '(%d,%d)'% (i,j)  
                tableWidget.setItem(i,j, QTableWidgetItem( itemContent ) )
        self.setLayout(conLayout)
        
        #遍历表查找对应的item
        text = "(19,1)"
        items = tableWidget.findItems(text, QtCore.Qt.MatchExactly)             
        item = items[0]
        #item.setSelected( True)
        
        item.setForeground(QBrush(QColor(255, 0, 0))) 
                
        row = item.row()   
        #滚轮定位过去，快速定位到第17行
        tableWidget.verticalScrollBar().setSliderPosition(row)  
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Table()  
    example.show()   
    sys.exit(app.exec_())
    