  update-icalendar:
    needs: validate-schedule
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v3
        with:
          python-version: 3.x
      - run: pip install pyyaml ics
      - name: Update iCalendar
        run: schedule/update-icalendar.py
      - name: Commit and push
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add schedule.ics
          git pull
          git commit -m "Auto-update calendar" || echo "No changes to commit"
          git push
