from mula_test_base import MulaTestBase 

class TestRemoveActivities(MulaTestBase):
    # duration = 14.580s
    def test_remove_activity_returns_sucess_message(self):
        # prepare test
        build_command = f"--database fup add {self.fup_act} -s 1"
        self.execute(self.build_command(build_command))
        
        # build commands
        command = f"--database fup rm -l {self.fup_act}"
        response = self.execute(self.build_command(command))
        
        # test results
        self.assertIn("@"+self.fup_act, response.stdout)

    # duration = 15.910s
    def test_remove_activity_changes_moodle(self):
        # prepare test
        build_command = f"--database fup add {self.fup_act} -s 1"
        self.execute(self.build_command(build_command))
        
        # build commands
        command = f"--database fup rm -l {self.fup_act}"
        self.execute(self.build_command(command))
        
        # test results
        list_command = f"--database fup list -s 1"
        response_list = self.execute(self.build_command(command))
        self.assertNotIn("@"+self.fup_act, response_list.stdout)

