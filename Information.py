import pandas as pd


class Information:
    # создание атрибутов класса
    countLecturer = 0
    lecturerCost = 0

    countStudents = 0
    trainingCost = 0

    countAccountant = 0
    trainingAccountant = 0

    internetCost = 0

    countSysAdmin = 0
    sysAdminCost = 0

    def ParseJson(self):
        try:
            patients_df = pd.read_json("C:\\offline.json")
            patients_df.head()
            return patients_df
        except Exception:
            print("Файл с данными не удалось прочитать!", Exception)

    def Start(self):
        offline = self.ParseJson()

        # Получения значения из JSON по названию ключа
        countLecturer = offline['CountLecturer'].values
        lecturerCost = offline['LecturerCost'].values

        countStudents = offline['CountStudents'].values
        trainingCost = offline['TrainingCost'].values

        countAccountant = offline['CountAccountant'].values
        trainingAccountant = offline['TrainingAccountant'].values

        internetCost = offline['InternetCost'].values

        countSysAdmin = offline['CountSysAdmin'].values
        sysAdminCost = offline['SysAdminCost'].values

        methodologistCost = offline['MethodologistCost'].values

