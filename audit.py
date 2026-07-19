import argparse
import csv
import json


def summarize(rows):
    grouped = {}
    for row in rows:
        key = (row["task"], row["subtask"])
        bucket = grouped.setdefault(key, {"sim": [], "real": [], "contact_errors": 0})
        domain = row["domain"].lower()
        bucket[domain].append(float(row["success"]))
        bucket["contact_errors"] += int(row["contact_error"])
    gaps = []
    for (task, subtask), values in grouped.items():
        if not values["sim"] or not values["real"]:
            continue
        sim_rate = sum(values["sim"]) / len(values["sim"])
        real_rate = sum(values["real"]) / len(values["real"])
        gaps.append({
            "task": task,
            "subtask": subtask,
            "sim_success_rate": round(sim_rate, 3),
            "real_success_rate": round(real_rate, 3),
            "absolute_gap": round(abs(sim_rate - real_rate), 3),
            "contact_errors": values["contact_errors"],
        })
    gaps.sort(key=lambda x: (-x["absolute_gap"], -x["contact_errors"], x["subtask"]))
    return {"paired_subtasks": len(gaps), "gaps": gaps}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output", default="report.json")
    args = parser.parse_args()
    with open(args.input, newline="", encoding="utf-8") as handle:
        report = summarize(list(csv.DictReader(handle)))
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2)
    print(f"ranked {report['paired_subtasks']} paired subtasks -> {args.output}")


if __name__ == "__main__":
    main()
