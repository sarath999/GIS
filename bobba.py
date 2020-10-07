from github import Github

g = Github('sarathchandra.bobba@gmail.com', '')

for repo in g.get_user().get_repos():
	print repo.name
	repo.edit(has_wiki=False)
