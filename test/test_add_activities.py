from mula_test_base import MulaTestBase 

class TestAddActivities(MulaTestBase):
    # duration = 13.163s
    def test_add_activity_returns_sucess_message(self):
        # build comand
        command = f"--database fup add {self.fup_act} -s 1"
        response = self.execute(self.build_command(command))
        
        # test results
        self.assertIn("@"+self.fup_act, response.stdout)
        
        # redo the changes
        change = f"--database fup rm -l {self.fup_act}"
        self.execute(self.build_command(change))

    # duration = 11.479s
    def test_add_activity_changes_moodle(self):
        # build command
        command = f"--database fup add {self.fup_act} -s 1"
        self.execute(self.build_command(command))
        
        # test results
        list_command = f"--database fup list -s 1"
        response_list = self.execute(self.build_command(list_command))
        self.assertIn("@"+self.fup_act, response_list.stdout)
        
        # redo the changes
        change = "--database fup rm -l {self.fup_act}"
        self.execute(self.build_command(change))

    # duration = 35.9s
    def test_add_activity_in_all_repositories_is_sucess(self):
        # prepare test
        add_fup_command = f"--database fup add {self.fup_act} -s 1"
        fup_response = self.execute(self.build_command(add_fup_command))

        add_ed_command = f"--database ed add {self.ed_act} -s 1"
        ed_response = self.execute(self.build_command(add_ed_command))

        add_poo_command = f"--database poo add {self.poo_act} -s 1"
        poo_response = self.execute(self.build_command(add_poo_command))

        # test results
        self.assertIn("@"+self.fup_act, fup_response.stdout)
        self.assertIn("@"+self.ed_act, ed_response.stdout)
        self.assertIn("@"+self.poo_act, poo_response.stdout)

        # redo the changes
        change = "--database fup rm --all"
        self.execute(self.build_command(change))

