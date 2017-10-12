# -*- coding:utf-8 -*-



# """
#     ����һ���ݹ麯����python��
#     ʹ�����ӣ�
# 
#     1 :get_value(dict, get_values_key)
# 
#         data = {"code": 0, "message": "�����ɹ�","result": {"amount": 950.0000,
#                 "totalBaoLiFee": None, "pageNo": 1,"data": [{"goodsId": 100}]}}
# 
#         print(get_value(data, "code"))
# 
# 
#     2: list_for_key_to_dict(*args, dict)
#         print(list_for_key_to_dict("code", "pageNo", "goodsId", my_dict=data))
# 
# """

class GetDictParam:
    """
        ����һ������dict ��������
        �������ڶ������ָ��key �� ָ��key���Ͻ���key
    """
    def __init__(self):
        """
            ��ʼ������
        """
        pass

    def get_value(self, my_dict, key):
        """
            ����һ���ݹ麯��
        """

        if isinstance(my_dict, dict):

            if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == ''\
                    and my_dict.get(key) is False:
                return my_dict.get(key)

            for my_dict_key in my_dict:
                if self.get_value(my_dict.get(my_dict_key), key) or \
                                self.get_value(my_dict.get(my_dict_key), key) is False:
                    return self.get_value(my_dict.get(my_dict_key), key)

        if isinstance(my_dict, list):
            for my_dict_arr in my_dict:
                if self.get_value(my_dict_arr, key) \
                        or self.get_value(my_dict_arr, key) is False:
                    return self.get_value(my_dict_arr, key)


    def list_for_key_to_dict(self, *args, my_dict):
        """
            ������Ҫ������dict�� ��Ҫ������Ҫ����my_dict��keys��list

        :param my_dict: ��Ҫ�������ֵ�
        :param args: ������Ҫ������key�Ķ���ַ���
            # list_for_key_to_dict("code", "pageNo", "goodsId", my_dict=dict)
        :return: һ������������ƴװ��dict
        """
        result = {}
        if len(args) > 0:
            for key in args:
                result.update({key: self.get_value(my_dict, key)})
        return result

