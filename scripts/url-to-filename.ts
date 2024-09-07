import { input, select } from '@inquirer/prompts'
import clipboardy from 'clipboardy'
import isWsl from 'is-wsl'
import childProcess from 'node:child_process'
import { promisify } from 'node:util'

const exec = promisify(childProcess.exec)

const copyToClipboard = async (value: string) => {
  try {
    if (isWsl) {
      await exec(`echo -n '${value}' | clip.exe`)
    } else {
      await clipboardy.write(value)
    }
    console.log(`Copied "${value}" to clipboard`)
  } catch (error) {
    console.error(`Error copying "${value}" to clipboard`)
  }
}

const urlToFileName = async () => {
  try {
    const url = await input({ message: 'Enter the LeetCode problem url:' })
    const problemName = url.split('/problems')[1].split('/')[1]

    const replacementChar = await select({
      message: 'Select a package manager',
      choices: [
        {
          value: '_',
          name: 'snake_case',
        },
        {
          value: '-',
          name: 'kebab-case',
        },
      ],
    })

    const fileName = problemName.toLowerCase()?.replace(/-/g, replacementChar)
    await copyToClipboard(fileName)
  } catch (error) {
    if (error.name === 'ExitPromptError') return
    console.error(error)
  }
}

const main = async () => {
  await urlToFileName()
}

main().catch(console.error)
