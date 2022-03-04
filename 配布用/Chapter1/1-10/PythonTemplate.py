import sys #sys はPythonの基礎的なライブラリです。 IronPythonの標準的なライブラリを読み込んでいる例です。
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib') #IronPythonの標準ライブラリをインポートしています。
#暗号化から正規表現までをカバーしています。
import System #.NETのSystemのルート
from System import Array #.NET classでarrayの機能を使うために読み込み
from System.Collections.Generic import * #ジェネリックを扱えるようにする RevitのAPI　は、ILists と呼ばれるハードタイプの「ジェネリック」リストを必要とすることがあります。

import clr #.NET's Common Language Runtimeです。 実行に必要な環境です。
clr.AddReference('ProtoGeometry')  #DynamoのライブラリでDynamoのジオメトリの処理を使うときに使用します。
from Autodesk.DesignScript.Geometry import * #Dynamoのジオメトリのライブラリを全て読み込む
clr.AddReference("RevitNodes") #Dynamoのノード（Revit用）

import Revit #RevitNodesのRevit namespace
clr.ImportExtensions(Revit.Elements) #DynamoのRevitのライブラリを読み込む（Element）
clr.ImportExtensions(Revit.GeometryConversion) #DynamoのRevitのライブラリを読み込む
clr.AddReference("RevitServices") #Revit documentsを扱うためのDynamoのクラス

import RevitServices 
from RevitServices.Persistence import DocumentManager #Dynamoのクラス
#DynamoがアタッチされたRevitのドキュメントをトラックする
from RevitServices.Transactions import TransactionManager #Dynamoのクラス
#トランザクションを開いたり閉じたりしてRevitのデータベースにアクセス

clr.AddReference("RevitAPI") #RevitのAPI DLLs
clr.AddReference("RevitAPIUI") #RevitのAPI DLLs

import Autodesk #Autodesk namespace
from Autodesk.Revit.DB import * #DBクラス
from Autodesk.Revit.UI import * #UIクラス

doc = DocumentManager.Instance.CurrentDBDocument #アクティブなRevitのドキュメント
uiapp = DocumentManager.Instance.CurrentUIApplication #アクティブなRevitのUIアプリケーション
app = uiapp.Application  #現在開いているRevitのアプリケーション
uidoc = uiapp.ActiveUIDocument #現在開いているRevitのUIドキュメント

#input = IN[0]
#Revitの要素として使う

element = UnwrapElement(IN[0])

#Transaction用のコード
TransactionManager.Instance.EnsureInTransaction(doc)
#RevitDocumentの変更内容をここに入れます
TransactionManager.Instance.TransactionTaskDone()

OUT = element