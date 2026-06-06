import argparse
import subprocess
from pathlib import Path


def typst_string(value):
    return str(value).replace('\\', '\\\\').replace('"', '\\"')


def typst_text(value):
    return str(value).replace("#", "\\#")


def display_end(value):
    return "Present" if str(value).lower() == "current" else str(value)


def date_range(start, end):
    return f"{start} - {display_end(end)}"


def load_resume(path):
    import yaml

    with Path(path).open("r", encoding="utf-8") as resume_file:
        return yaml.safe_load(resume_file)


def validate_resume(data):
    if not isinstance(data, dict):
        raise ValueError("resume data must be a mapping")

    for key in ("basics", "experience", "education"):
        if key not in data:
            raise ValueError(f"missing required top-level key: {key}")

    if "name" not in data["basics"]:
        raise ValueError("missing required basics.name")

    for company_index, company in enumerate(data["experience"]):
        if "company" not in company:
            raise ValueError(f"experience[{company_index}] is missing company")
        if "roles" not in company:
            raise ValueError(f"experience[{company_index}] is missing roles")
        for role_index, role in enumerate(company["roles"]):
            for key in ("title", "start", "end", "highlights"):
                if key not in role:
                    raise ValueError(
                        f"experience[{company_index}].roles[{role_index}] is missing {key}"
                    )


def render_header(basics):
    fields = [
        ("author", basics["name"]),
        ("location", basics.get("location")),
        ("email", basics.get("email")),
        ("github", basics.get("github")),
        ("linkedin", basics.get("linkedin")),
        ("phone", basics.get("phone")),
        ("personal-site", basics.get("website")),
    ]
    lines = ['#import "@preview/basic-resume:0.2.9": *', "", "#show: resume.with("]
    for key, value in fields:
        if value:
            lines.append(f'  {key}: "{typst_string(value)}",')
    lines.extend(
        [
            '  accent-color: "#26428b",',
            '  font: "Georgia",',
            '  paper: "us-letter",',
            "  author-position: center,",
            "  personal-info-position: center,",
            ")",
        ]
    )
    return "\n".join(lines)


def render_experience(experience):
    lines = ["== Work Experience", ""]
    for company in experience:
        for role in company["roles"]:
            location = role.get("location", company.get("location", ""))
            lines.extend(
                [
                    "#grid(",
                    "  columns: (1fr, auto),",
                    f"  [*{typst_text(company['company'])}* - {typst_text(role['title'])}],",
                    f"  [{typst_text(date_range(role['start'], role['end']))}],",
                    ")",
                ]
            )
            if location:
                lines.append(f"#align(right)[{typst_text(location)}]")
            for highlight in role["highlights"]:
                lines.append(f"- {typst_text(highlight)}")
            if role.get("tech"):
                lines.append(f"- *Key Tech* - {typst_text(', '.join(role['tech']))}")
            lines.extend(["#v(0.35em)", ""])
    return "\n".join(lines).rstrip()


def render_projects(projects):
    lines = ["== Projects", ""]
    for project in projects:
        heading = f"*{typst_text(project['name'])}*"
        if project.get("link"):
            heading = f"{heading} - {typst_text(project['link'])}"
        lines.append(heading)
        if project.get("summary"):
            lines.append(typst_text(project["summary"]))
        for highlight in project.get("highlights", []):
            lines.append(f"- {typst_text(highlight)}")
        if project.get("tech"):
            lines.append(f"- *Key Tech* - {typst_text(', '.join(project['tech']))}")
        lines.extend(["#v(0.35em)", ""])
    return "\n".join(lines).rstrip()


def render_education(education):
    lines = ["== Education", ""]
    for item in education:
        degree = item.get("degree", "")
        field = item.get("field", "")
        degree_text = ", ".join(part for part in (degree, field) if part)
        lines.extend(
            [
                "#edu(",
                f'  institution: "{typst_string(item["school"])}",',
                f'  location: "{typst_string(item.get("location", ""))}",',
                f'  dates: dates-helper(start-date: "{typst_string(item.get("start", ""))}", end-date: "{typst_string(item.get("end", ""))}"),',
                f'  degree: "{typst_string(degree_text)}",',
                ")",
            ]
        )
        for highlight in item.get("highlights", []):
            lines.append(f"- {typst_text(highlight)}")
        lines.append("")
    return "\n".join(lines).rstrip()


def render_resume(data):
    validate_resume(data)
    sections = [
        render_header(data["basics"]),
        render_experience(data["experience"]),
    ]
    if data.get("projects"):
        sections.append(render_projects(data["projects"]))
    sections.extend([render_education(data["education"]), ""])
    return "\n\n".join(
        sections
    )


def compile_typst(input_path, output_path):
    subprocess.run(["typst", "compile", str(input_path), str(output_path)], check=True)


def main():
    parser = argparse.ArgumentParser(description="Build a Typst resume from YAML data.")
    parser.add_argument("--input", default="resume.yaml")
    parser.add_argument("--output", default="resume.typ")
    parser.add_argument("--pdf", default="resume.pdf")
    parser.add_argument("--no-compile", action="store_true")
    args = parser.parse_args()

    data = load_resume(args.input)
    rendered = render_resume(data)
    Path(args.output).write_text(rendered, encoding="utf-8")

    if not args.no_compile:
        compile_typst(args.output, args.pdf)


if __name__ == "__main__":
    main()
