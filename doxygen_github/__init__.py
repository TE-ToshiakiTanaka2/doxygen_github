""" A short description of the project """
## @package doxygen_github
# Document for this module.
#
# Doxygen用のSampleパッケージです．
__version__ = "0.1.0"

## get_version : Version情報の取得
#
# Doxygen用のSample Function名です．
def get_version():
    return __version__



## @class Sample Class
#
# Detail Sample Class Name.
# @brief 説明(簡単)
# @details 説明（詳細）
# @warning 警告メッセージ
# @note メモ
class Sample:
    def __init__(self):
        ##
        # @fn __init__()
        # @brief 説明(簡単) [例：クラスの初期化メソッド（コンストラクタ）]
        # @param 引数の説明
        # @return 戻り値の詳細（例：None 戻り値なし）
        # @retval 戻り値の詳細：複数ある場合（例：sum_ab aとbの和（float））
        # @retval 戻り値の詳細：複数ある場合（例：sub_ab aとbの差（float））
        # @details 説明（詳細）
        # @warning 警告メッセージ
        # @note メモ
