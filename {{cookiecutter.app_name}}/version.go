package main

// GitCommit is the git commit from which this that binary was compiled.
// This will be filled in by the compiler.
const GitCommit = ""

// Version is the tag from which this binary was compiled.
const Version = ""

// VersionPrerelease is a pre-release marker for the version of this binary.
// If this is "" (empty string) then it means that it is a final release.
// Otherwise, this is a pre-release such as "dev" (in development)
const VersionPrerelease = ""
