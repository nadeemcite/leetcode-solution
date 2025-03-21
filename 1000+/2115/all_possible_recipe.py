class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        available_supplies = set(supplies)
        
        recipe_to_ingredients = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        
        visited = {}
        result = []
        
        def can_make(recipe):
            if recipe in visited and visited[recipe] == 0:
                return False
                
            if recipe in visited and visited[recipe] == 1:
                return True
                
            if recipe in available_supplies:
                return True
                
            if recipe not in recipe_to_ingredients:
                return False
                
            visited[recipe] = 0
            
            for ingredient in recipe_to_ingredients[recipe]:
                if not can_make(ingredient):
                    visited[recipe] = -1
                    return False
                    
            visited[recipe] = 1
            result.append(recipe)
            return True
        
        for recipe in recipes:
            can_make(recipe)
        
        return [recipe for recipe in recipes if recipe in visited and visited[recipe]== 1]
           
        


print(Solution().findAllRecipes(["apple pie", "apple tart", "apple crumble"], [["apple", "flour", "sugar"], ["apple", "flour", "sugar"], ["apple", "flour", "sugar"]], ["apple", "flour", "sugar"]))



print(Solution().findAllRecipes(["apple pie", "apple tart", "apple crumble"], [["apple", "flour", "sugar"], ["apple", "flour", "sugar"], ["apple", "flour", "sugar"]], ["apple", "flour", "sugar"]))

print(Solution().findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour","corn"]))