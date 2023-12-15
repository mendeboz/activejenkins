from os import listdir, getcwd
import subprocess

GREEN_HIGHLIGHT = '6;30;42m'
YELLOW_HIGHLIGHT = '5;31;43m'

REPOS = listdir('hudsonmx')

for _, repo_name in enumerate(REPOS):
  repo = getcwd() + '/hudsonmx/' + repo_name + '/'
  # Green color - checkpoint
  print('\x1b[%s' % (GREEN_HIGHLIGHT) + repo_name + '\x1b[0m')

  # git_branch = subprocess.Popen(
  #   ['git', '-C', repo, 'branch'],
  #   stdout=subprocess.PIPE,
  #   stderr=subprocess.PIPE,
  #   universal_newlines=True, bufsize=1
  # )
  # out, err = git_branch.communicate()
  # print(out)
  # # Warning colored error message
  # print('\x1b[%s' % (YELLOW_HIGHLIGHT) + err + '\x1b[0m')

  git_status = subprocess.Popen(
    ['git', '-C', repo, 'status'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True, bufsize=1
  )
  out, err = git_status.communicate()
  if 'modified' in out:
    git_commit = subprocess.Popen(
      ['git', '-C', repo, 'commit', '-a', '-m', 'Fix release artifact Jenkins job'],
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      universal_newlines=True, bufsize=1
    )
    out, err = git_commit.communicate()
    print(out)
    # Warning colored error message
    print('\x1b[%s' % (YELLOW_HIGHLIGHT) + err + '\x1b[0m')

    git_push = subprocess.Popen(
      ['git', '-C', repo, 'push'],
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      universal_newlines=True, bufsize=1
    )
    out, err = git_push.communicate()
    print(out)
    # Warning colored error message
    print('\x1b[%s' % (YELLOW_HIGHLIGHT) + err + '\x1b[0m')

print('\x1b[%s' % (GREEN_HIGHLIGHT) + 'END' + '\x1b[0m')