class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        preferences = [0, 0]
        for preference in students:
            preferences[preference] += 1

        for sandwich in sandwiches:

            if preferences[sandwich] == 0:
                return sum(preferences)

            preferences[sandwich] -= 1
        return 0

