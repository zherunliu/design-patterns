# from typing import Optional
import threading

# # hungry mode
# class Singleton:
#     instance = None

#     def __init__(self) -> None:
#         if Singleton.instance is not None:
#             raise Exception("Only one instance of Singleton class is allowed.")
#         else:
#             Singleton.instance = self


# # lazy mode
# class Singleton:
#     __instance: Optional['Singleton'] = None # 双下划线表示私有变量

#     @staticmethod
#     def getInstance():
#         if Singleton.__instance is None:
#             Singleton.__instance = Singleton()
#         return Singleton.__instance


# lazy mode with Double-Checked Locking
class Singleton:
    __instance = None
    __lock = threading.Lock()

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            with cls.__lock:  # 保证线程安全，同一时刻内只有一个线程可以创建单例
                if (
                    cls.__instance is None
                ):  # 二次检查，防止等待锁的过程中，其他线程已经创建了实例
                    cls.__instance = Singleton()
        return cls.__instance
