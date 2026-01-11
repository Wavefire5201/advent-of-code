with open("input.txt") as f:
    lines = f.readlines()
    id_section = False
    fresh = 0
    ranges = []
    for i, line in enumerate(lines):
        line = line.strip()
        if line == "":
            id_section = True
            continue

        if id_section:
            for l, r in ranges:
                if int(line) >= l and int(line) <= r:
                    fresh += 1
                    break
        else:
            pl, pr = line.split("-")
            pl, pr = int(pl), int(pr)
            ranges.append((pl, pr))

    print(fresh)

    ranges.sort()
    merged_ranges = []
    if ranges:
        curr_start, curr_end = ranges[0]

        for i in range(1, len(ranges)):
            next_start, next_end = ranges[i]

            if next_start <= curr_end:  # Overlap found!
                # Extend the current end if the next one goes further
                curr_end = max(curr_end, next_end)
            else:
                # No overlap, so push the completed range and start a new one
                merged_ranges.append((curr_start, curr_end))
                curr_start, curr_end = next_start, next_end

        # Append the final range
        merged_ranges.append((curr_start, curr_end))

    # 3. Calculate the total count
    total_fresh = 0
    for start, end in merged_ranges:
        total_fresh += end - start + 1

    print(total_fresh)
