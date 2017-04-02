from github import Github

g = Github('sarathchandra.bobba@gmail.com', 'iton@123')

for repo in g.get_user().get_repos():
	print repo.name
	repo.edit(has_wiki=False)
